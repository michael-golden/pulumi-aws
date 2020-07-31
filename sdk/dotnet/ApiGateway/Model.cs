// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.ApiGateway
{
    /// <summary>
    /// Provides a Model for a REST API Gateway.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var myDemoAPI = new Aws.ApiGateway.RestApi("myDemoAPI", new Aws.ApiGateway.RestApiArgs
    ///         {
    ///             Description = "This is my API for demonstration purposes",
    ///         });
    ///         var myDemoModel = new Aws.ApiGateway.Model("myDemoModel", new Aws.ApiGateway.ModelArgs
    ///         {
    ///             RestApi = myDemoAPI.Id,
    ///             Description = "a JSON schema",
    ///             ContentType = "application/json",
    ///             Schema = @"{
    ///   ""type"": ""object""
    /// }
    /// ",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class Model : Pulumi.CustomResource
    {
        /// <summary>
        /// The content type of the model
        /// </summary>
        [Output("contentType")]
        public Output<string> ContentType { get; private set; } = null!;

        /// <summary>
        /// The description of the model
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The name of the model
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The ID of the associated REST API
        /// </summary>
        [Output("restApi")]
        public Output<string> RestApi { get; private set; } = null!;

        /// <summary>
        /// The schema of the model in a JSON form
        /// </summary>
        [Output("schema")]
        public Output<string?> Schema { get; private set; } = null!;


        /// <summary>
        /// Create a Model resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Model(string name, ModelArgs args, CustomResourceOptions? options = null)
            : base("aws:apigateway/model:Model", name, args ?? new ModelArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Model(string name, Input<string> id, ModelState? state = null, CustomResourceOptions? options = null)
            : base("aws:apigateway/model:Model", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Model resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Model Get(string name, Input<string> id, ModelState? state = null, CustomResourceOptions? options = null)
        {
            return new Model(name, id, state, options);
        }
    }

    public sealed class ModelArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The content type of the model
        /// </summary>
        [Input("contentType", required: true)]
        public Input<string> ContentType { get; set; } = null!;

        /// <summary>
        /// The description of the model
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the model
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the associated REST API
        /// </summary>
        [Input("restApi", required: true)]
        public Input<string> RestApi { get; set; } = null!;

        /// <summary>
        /// The schema of the model in a JSON form
        /// </summary>
        [Input("schema")]
        public Input<string>? Schema { get; set; }

        public ModelArgs()
        {
        }
    }

    public sealed class ModelState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The content type of the model
        /// </summary>
        [Input("contentType")]
        public Input<string>? ContentType { get; set; }

        /// <summary>
        /// The description of the model
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the model
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the associated REST API
        /// </summary>
        [Input("restApi")]
        public Input<string>? RestApi { get; set; }

        /// <summary>
        /// The schema of the model in a JSON form
        /// </summary>
        [Input("schema")]
        public Input<string>? Schema { get; set; }

        public ModelState()
        {
        }
    }
}
