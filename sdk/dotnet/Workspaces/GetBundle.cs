// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Workspaces
{
    public static class GetBundle
    {
        /// <summary>
        /// Retrieve information about an AWS WorkSpaces bundle.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Aws = Pulumi.Aws;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var example = Output.Create(Aws.Workspaces.GetBundle.InvokeAsync(new Aws.Workspaces.GetBundleArgs
        ///         {
        ///             Name = "Value with Windows 10 and Office 2016",
        ///             Owner = "AMAZON",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetBundleResult> InvokeAsync(GetBundleArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetBundleResult>("aws:workspaces/getBundle:getBundle", args ?? new GetBundleArgs(), options.WithVersion());
    }


    public sealed class GetBundleArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the bundle.
        /// </summary>
        [Input("bundleId")]
        public string? BundleId { get; set; }

        /// <summary>
        /// The name of the bundle. You cannot combine this parameter with `bundle_id`.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// The owner of the bundles. You have to leave it blank for own bundles. You cannot combine this parameter with `bundle_id`.
        /// </summary>
        [Input("owner")]
        public string? Owner { get; set; }

        public GetBundleArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetBundleResult
    {
        /// <summary>
        /// The ID of the bundle.
        /// </summary>
        public readonly string? BundleId;
        /// <summary>
        /// The compute type. See supported fields below.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetBundleComputeTypeResult> ComputeTypes;
        /// <summary>
        /// The description of the bundle.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The name of the compute type.
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// The owner of the bundle.
        /// </summary>
        public readonly string? Owner;
        /// <summary>
        /// The root volume. See supported fields below.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetBundleRootStorageResult> RootStorages;
        /// <summary>
        /// The user storage. See supported fields below.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetBundleUserStorageResult> UserStorages;

        [OutputConstructor]
        private GetBundleResult(
            string? bundleId,

            ImmutableArray<Outputs.GetBundleComputeTypeResult> computeTypes,

            string description,

            string id,

            string? name,

            string? owner,

            ImmutableArray<Outputs.GetBundleRootStorageResult> rootStorages,

            ImmutableArray<Outputs.GetBundleUserStorageResult> userStorages)
        {
            BundleId = bundleId;
            ComputeTypes = computeTypes;
            Description = description;
            Id = id;
            Name = name;
            Owner = owner;
            RootStorages = rootStorages;
            UserStorages = userStorages;
        }
    }
}
