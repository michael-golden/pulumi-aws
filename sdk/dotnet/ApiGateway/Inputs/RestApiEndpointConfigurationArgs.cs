// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.ApiGateway.Inputs
{

    public sealed class RestApiEndpointConfigurationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A list of endpoint types. This resource currently only supports managing a single value. Valid values: `EDGE`, `REGIONAL` or `PRIVATE`. If unspecified, defaults to `EDGE`. Must be declared as `REGIONAL` in non-Commercial partitions. Refer to the [documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/create-regional-api.html) for more information on the difference between edge-optimized and regional APIs.
        /// </summary>
        [Input("types", required: true)]
        public Input<string> Types { get; set; } = null!;

        [Input("vpcEndpointIds")]
        private InputList<string>? _vpcEndpointIds;

        /// <summary>
        /// A list of VPC Endpoint Ids. It is only supported for PRIVATE endpoint type.
        /// </summary>
        public InputList<string> VpcEndpointIds
        {
            get => _vpcEndpointIds ?? (_vpcEndpointIds = new InputList<string>());
            set => _vpcEndpointIds = value;
        }

        public RestApiEndpointConfigurationArgs()
        {
        }
    }
}