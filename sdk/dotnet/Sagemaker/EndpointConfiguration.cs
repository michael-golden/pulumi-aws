// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Sagemaker
{
    /// <summary>
    /// Provides a SageMaker endpoint configuration resource.
    /// 
    /// 
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sagemaker_endpoint_configuration.html.markdown.
    /// </summary>
    public partial class EndpointConfiguration : Pulumi.CustomResource
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) assigned by AWS to this endpoint configuration.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Amazon Resource Name (ARN) of a AWS Key Management Service key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint.
        /// </summary>
        [Output("kmsKeyArn")]
        public Output<string?> KmsKeyArn { get; private set; } = null!;

        /// <summary>
        /// The name of the endpoint configuration. If omitted, this provider will assign a random, unique name.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Fields are documented below.
        /// </summary>
        [Output("productionVariants")]
        public Output<ImmutableArray<Outputs.EndpointConfigurationProductionVariants>> ProductionVariants { get; private set; } = null!;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a EndpointConfiguration resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public EndpointConfiguration(string name, EndpointConfigurationArgs args, CustomResourceOptions? options = null)
            : base("aws:sagemaker/endpointConfiguration:EndpointConfiguration", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private EndpointConfiguration(string name, Input<string> id, EndpointConfigurationState? state = null, CustomResourceOptions? options = null)
            : base("aws:sagemaker/endpointConfiguration:EndpointConfiguration", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing EndpointConfiguration resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static EndpointConfiguration Get(string name, Input<string> id, EndpointConfigurationState? state = null, CustomResourceOptions? options = null)
        {
            return new EndpointConfiguration(name, id, state, options);
        }
    }

    public sealed class EndpointConfigurationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of a AWS Key Management Service key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint.
        /// </summary>
        [Input("kmsKeyArn")]
        public Input<string>? KmsKeyArn { get; set; }

        /// <summary>
        /// The name of the endpoint configuration. If omitted, this provider will assign a random, unique name.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("productionVariants", required: true)]
        private InputList<Inputs.EndpointConfigurationProductionVariantsArgs>? _productionVariants;

        /// <summary>
        /// Fields are documented below.
        /// </summary>
        public InputList<Inputs.EndpointConfigurationProductionVariantsArgs> ProductionVariants
        {
            get => _productionVariants ?? (_productionVariants = new InputList<Inputs.EndpointConfigurationProductionVariantsArgs>());
            set => _productionVariants = value;
        }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public EndpointConfigurationArgs()
        {
        }
    }

    public sealed class EndpointConfigurationState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) assigned by AWS to this endpoint configuration.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// Amazon Resource Name (ARN) of a AWS Key Management Service key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint.
        /// </summary>
        [Input("kmsKeyArn")]
        public Input<string>? KmsKeyArn { get; set; }

        /// <summary>
        /// The name of the endpoint configuration. If omitted, this provider will assign a random, unique name.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("productionVariants")]
        private InputList<Inputs.EndpointConfigurationProductionVariantsGetArgs>? _productionVariants;

        /// <summary>
        /// Fields are documented below.
        /// </summary>
        public InputList<Inputs.EndpointConfigurationProductionVariantsGetArgs> ProductionVariants
        {
            get => _productionVariants ?? (_productionVariants = new InputList<Inputs.EndpointConfigurationProductionVariantsGetArgs>());
            set => _productionVariants = value;
        }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public EndpointConfigurationState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class EndpointConfigurationProductionVariantsArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The size of the Elastic Inference (EI) instance to use for the production variant.
        /// </summary>
        [Input("acceleratorType")]
        public Input<string>? AcceleratorType { get; set; }

        /// <summary>
        /// Initial number of instances used for auto-scaling.
        /// </summary>
        [Input("initialInstanceCount", required: true)]
        public Input<int> InitialInstanceCount { get; set; } = null!;

        /// <summary>
        /// Determines initial traffic distribution among all of the models that you specify in the endpoint configuration. If unspecified, it defaults to 1.0.
        /// </summary>
        [Input("initialVariantWeight")]
        public Input<double>? InitialVariantWeight { get; set; }

        /// <summary>
        /// The type of instance to start.
        /// </summary>
        [Input("instanceType", required: true)]
        public Input<string> InstanceType { get; set; } = null!;

        /// <summary>
        /// The name of the model to use.
        /// </summary>
        [Input("modelName", required: true)]
        public Input<string> ModelName { get; set; } = null!;

        /// <summary>
        /// The name of the variant. If omitted, this provider will assign a random, unique name.
        /// </summary>
        [Input("variantName")]
        public Input<string>? VariantName { get; set; }

        public EndpointConfigurationProductionVariantsArgs()
        {
        }
    }

    public sealed class EndpointConfigurationProductionVariantsGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The size of the Elastic Inference (EI) instance to use for the production variant.
        /// </summary>
        [Input("acceleratorType")]
        public Input<string>? AcceleratorType { get; set; }

        /// <summary>
        /// Initial number of instances used for auto-scaling.
        /// </summary>
        [Input("initialInstanceCount", required: true)]
        public Input<int> InitialInstanceCount { get; set; } = null!;

        /// <summary>
        /// Determines initial traffic distribution among all of the models that you specify in the endpoint configuration. If unspecified, it defaults to 1.0.
        /// </summary>
        [Input("initialVariantWeight")]
        public Input<double>? InitialVariantWeight { get; set; }

        /// <summary>
        /// The type of instance to start.
        /// </summary>
        [Input("instanceType", required: true)]
        public Input<string> InstanceType { get; set; } = null!;

        /// <summary>
        /// The name of the model to use.
        /// </summary>
        [Input("modelName", required: true)]
        public Input<string> ModelName { get; set; } = null!;

        /// <summary>
        /// The name of the variant. If omitted, this provider will assign a random, unique name.
        /// </summary>
        [Input("variantName")]
        public Input<string>? VariantName { get; set; }

        public EndpointConfigurationProductionVariantsGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class EndpointConfigurationProductionVariants
    {
        /// <summary>
        /// The size of the Elastic Inference (EI) instance to use for the production variant.
        /// </summary>
        public readonly string? AcceleratorType;
        /// <summary>
        /// Initial number of instances used for auto-scaling.
        /// </summary>
        public readonly int InitialInstanceCount;
        /// <summary>
        /// Determines initial traffic distribution among all of the models that you specify in the endpoint configuration. If unspecified, it defaults to 1.0.
        /// </summary>
        public readonly double? InitialVariantWeight;
        /// <summary>
        /// The type of instance to start.
        /// </summary>
        public readonly string InstanceType;
        /// <summary>
        /// The name of the model to use.
        /// </summary>
        public readonly string ModelName;
        /// <summary>
        /// The name of the variant. If omitted, this provider will assign a random, unique name.
        /// </summary>
        public readonly string VariantName;

        [OutputConstructor]
        private EndpointConfigurationProductionVariants(
            string? acceleratorType,
            int initialInstanceCount,
            double? initialVariantWeight,
            string instanceType,
            string modelName,
            string variantName)
        {
            AcceleratorType = acceleratorType;
            InitialInstanceCount = initialInstanceCount;
            InitialVariantWeight = initialVariantWeight;
            InstanceType = instanceType;
            ModelName = modelName;
            VariantName = variantName;
        }
    }
    }
}
